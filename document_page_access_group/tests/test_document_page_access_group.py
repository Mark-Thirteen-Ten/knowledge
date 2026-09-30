# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.exceptions import AccessError, UserError
from odoo.tests.common import users

from .common import TestDocumentPageAccessGroupBase


class TestDocumentPageAccessGroup(TestDocumentPageAccessGroupBase):
    def test_page_access_constrains(self):
        with self.assertRaises(UserError):
            self.knowledge_page.write({"user_ids": [(6, 0, [self.user.id])]})

    @users("test-user")
    def test_page_access_01(self):
        pages = self.env["document.page"].search([])
        self.assertIn(self.public_page, pages)
        self.assertNotIn(self.knowledge_page, pages)
        self.assertIn(self.user_page, pages)

    @users("test-manager-user")
    def test_page_access_02(self):
        pages = self.env["document.page"].search([])
        self.assertIn(self.public_page, pages)
        self.assertIn(self.knowledge_page, pages)
        self.assertNotIn(self.user_page, pages)

    @users("test-editor-user")
    def test_editor_access_in_category(self):
        pages = self.env["document.page"].search([])
        self.assertIn(self.knowledge_category_page, pages)
        self.assertNotIn(self.other_category_page, pages)
        self.knowledge_category_page.with_user(self.editor_user).write(
            {"name": "Edited page in Knowledge Category"}
        )
        with self.assertRaises(AccessError):
            self.other_category_page.with_user(self.editor_user).write(
                {"name": "Should not be editable"}
            )
