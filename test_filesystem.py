import unittest
import os
import json
from filesystem_project import FileSystem, Node 

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.json_file = 'test_fs_data.json'
        if os.path.exists(self.json_file):
            os.remove(self.json_file)
        
        self.fs = FileSystem(json_file=self.json_file)
        self.fs.root.children = {} 
        self.fs.node_map = {self.fs.root.id: self.fs.root}
        self.fs.trie_root = self.fs.trie_root.__class__() 
        self.fs.trash_can = {}

        self.fs.create_node("/", "Documentos", "carpeta")
        self.fs.create_node("/Documentos", "Tesis.pdf", "archivo")
        self.fs.create_node("/Documentos", "Borradores", "carpeta")
        self.fs.create_node("/", "Fotos", "carpeta")

    def tearDown(self):
        if os.path.exists(self.json_file):
            os.remove(self.json_file)

    def test_a_create_and_retrieve_node(self):
        self.assertIsNotNone(self.fs.get_node_by_path("/Documentos/Tesis.pdf"))
        self.assertIsNone(self.fs.get_node_by_path("/Documentos/Inexistente/archivo.txt"))
        initial_count = len(self.fs.get_node_by_path("/Documentos").children)
        self.fs.create_node("/Documentos", "Tesis.pdf", "archivo") 
        final_count = len(self.fs.get_node_by_path("/Documentos").children)
        self.assertEqual(initial_count, final_count)

    def test_b_rename_node_and_path_update(self):
        self.fs.rename_node("/Documentos/Tesis.pdf", "Proyecto_Final.pdf")
        self.assertIsNone(self.fs.get_node_by_path("/Documentos/Tesis.pdf"))
        self.assertIsNotNone(self.fs.get_node_by_path("/Documentos/Proyecto_Final.pdf"))

    def test_c_move_node_consistency_and_parent_update(self):
        self.fs.move_node("/Documentos/Tesis.pdf", "/Fotos")
        self.assertIsNone(self.fs.get_node_by_path("/Documentos/Tesis.pdf"))
        moved_node = self.fs.get_node_by_path("/Fotos/Tesis.pdf")
        self.assertIsNotNone(moved_node)
        self.assertEqual(moved_node.parent.nombre, "Fotos")

    def test_d_move_node_to_own_subdirectory_failure(self):
        result = self.fs.move_node("/Documentos", "/Documentos/Borradores")
        self.assertFalse(result)
        self.assertIsNotNone(self.fs.get_node_by_path("/Documentos"))

    def test_e_persistence_load_and_parent_references(self):
        self.fs._save_to_json()
        new_fs = FileSystem(json_file=self.json_file)
        loaded_node = new_fs.get_node_by_path("/Documentos/Tesis.pdf")
        self.assertEqual(loaded_node.parent.nombre, "Documentos")
        self.assertEqual(new_fs.show_full_path(loaded_node.parent), "/Documentos")

    def test_f_preorder_export_correctness(self):
        preorder_list = self.fs.export_preorder("/")
        self.assertTrue("[CARPETA] /" in preorder_list[0])
        self.assertTrue("/Documentos" in preorder_list[1])
        self.assertTrue("/Documentos/Borradores" in preorder_list[2])
        self.assertTrue("/Documentos/Tesis.pdf" in preorder_list[3])
        self.assertTrue("/Fotos" in preorder_list[4])

    def test_g_search_by_prefix_and_trie_update_on_rename(self):
        self.fs.rename_node("/Documentos/Tesis.pdf", "Trabajo_Final.pdf")
        old_results = self.fs.search_by_prefix("Tes")
        self.assertEqual(len(old_results), 0)
        new_results = self.fs.search_by_prefix("Trab")
        self.assertEqual(len(new_results), 1)
        self.assertEqual(new_results[0]['nombre'], "Trabajo_Final.pdf")

    def test_h_soft_delete_and_trie_update(self):
        node_to_delete = self.fs.get_node_by_path("/Documentos/Tesis.pdf")
        self.fs.delete_node("/Documentos/Tesis.pdf")
        self.assertTrue(node_to_delete.id in self.fs.trash_can)
        self.assertIsNone(self.fs.get_node_by_path("/Documentos/Tesis.pdf"))
        results = self.fs.search_by_prefix("Tes")
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)