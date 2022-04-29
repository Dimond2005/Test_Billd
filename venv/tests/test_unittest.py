import unittest
from main import documents, check_document_existance, get_doc_owner_name, get_all_doc_owners_names, \
    get_all_doc_owners_names
from main import add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, move_doc_to_shelf, show_document_info, \
    add_new_doc
from yandex import YaUploader, uploader


class TestFunction(unittest.TestCase):
    def setUp(self):
        print("Метод setUp")

    def tearDown(self) -> None:
        print('Метод tearDown')

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('10006'), 'Аристарх Павлов')

    def test_check_document_existance(self):
        self.assertEqual(check_document_existance('10006'), True)

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('11-2', '4'), ('11-2', '4'))

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('10006'), ('2'))

    def test_move_doc_to_shelf(self):
        self.assertEqual(move_doc_to_shelf('10006', '3'), ('10006', '3'))

    def test_show_document_info(self):
        self.assertEqual(show_document_info(documents[0]), ("passport", "2207 876234", "Василий Гупкин"))

    def test_delete_doc(self):
        self.assertEqual(delete_doc('11-2'), ('11-2', True))

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Аристарх Павлов', 'Геннадий Покемонов', 'Василий Гупкин'})

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('11-2', "invoice", "Геннадий Покемонов", "1"),
                         {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"})

    def test_upload(self):
        self.assertEqual(YaUploader('AQAAAAAekZYcAADLW0T0fkUJckWehsgTKNr20iA').upload('dishes.txt', 'dishes.txt'), 201)
