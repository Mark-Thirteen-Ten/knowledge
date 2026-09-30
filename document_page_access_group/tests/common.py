# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo.tests import new_test_user

from odoo.addons.base.tests.common import BaseCommon


class TestDocumentPageAccessGroupBase(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = cls.env["res.groups"].create({"name": "Test group"})
        cls.other_group = cls.env["res.groups"].create({"name": "Other test group"})
        cls.user = new_test_user(
            cls.env, login="test-user", groups="document_knowledge.group_document_user"
        )
        cls.editor_user = new_test_user(
            cls.env,
            login="test-editor-user",
            groups="document_page.group_document_editor",
        )
        cls.manager_user = new_test_user(
            cls.env,
            login="test-manager-user",
            groups="document_knowledge.group_document_user",
        )
        cls.manager_user.write({"groups_id": [(4, cls.group.id)]})
        cls.public_page = cls.env["document.page"].create(
            {"name": "Public Page", "type": "content"}
        )
        cls.knowledge_page = cls.env["document.page"].create(
            {
                "name": "Knowledge Page",
                "type": "content",
                "groups_id": [(6, 0, [cls.group.id])],
            }
        )
        cls.knowledge_category = cls.env["document.page"].create(
            {
                "name": "Knowledge Category",
                "type": "category",
                "groups_id": [(6, 0, [cls.group.id])],
            }
        )
        cls.knowledge_category_page = cls.env["document.page"].create(
            {"name": "Page in Knowledge Category", "parent_id": cls.knowledge_category.id}
        )
        cls.other_category = cls.env["document.page"].create(
            {
                "name": "Other Category",
                "type": "category",
                "groups_id": [(6, 0, [cls.other_group.id])],
            }
        )
        cls.other_category_page = cls.env["document.page"].create(
            {"name": "Page in Other Category", "parent_id": cls.other_category.id}
        )
        cls.user_page = cls.env["document.page"].create(
            {
                "name": "User Page (basic user)",
                "type": "content",
                "user_ids": [(6, 0, [cls.user.id])],
            }
        )
