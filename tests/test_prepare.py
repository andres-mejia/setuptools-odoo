# -*- coding: utf-8 -*-
# © 2015 ACSONE SA/NV
# License LGPLv3 (http://www.gnu.org/licenses/lgpl-3.0-standalone.html)
import os
import unittest

from setuptools_odoo.core import (
    prepare_odoo_addon,
    prepare_odoo_addons,
)

from . import DATA_DIR, working_directory_keeper


class TestPrepare(unittest.TestCase):
    """ Test the prepare... public api """

    def test_addon1(self):
        addon_dir = os.path.join(DATA_DIR, 'setup_reusable_addons', 'addon1')
        with working_directory_keeper:
            os.chdir(addon_dir)
            keywords = prepare_odoo_addon()
            self.assertEquals(keywords, {
                'description': 'addon 1 summary',
                'include_package_data': True,
                'install_requires': ['odoo>=8.0a,<9.0a'],
                'license': 'AGPL-3',
                'long_description': 'addon 1 readme content\n',
                'name': 'odoo-addon-addon1',
                'namespace_packages': ['odoo_addons'],
                'packages': ['odoo_addons'],
                'url': 'https://acsone.eu/',
                'version': '8.0.1.0.0',
                'zip_safe': False,
            })

    def test_addon2(self):
        addon_dir = os.path.join(DATA_DIR, 'setup_reusable_addons', 'addon2')
        with working_directory_keeper:
            os.chdir(addon_dir)
            keywords = prepare_odoo_addon()
            self.assertEquals(keywords, {
                'description': 'addon 2 summary',
                'include_package_data': True,
                'install_requires': ['odoo-addon-addon1>=8.0a,<9.0a',
                                     'odoo>=8.0a,<9.0a',
                                     'python-dateutil'],
                'name': 'odoo-addon-addon2',
                'namespace_packages': ['odoo_addons'],
                'packages': ['odoo_addons'],
                'version': '8.0.1.0.1',
                'zip_safe': False,
            })

    def test_addons_dir(self):
        addons_dir = os.path.join(DATA_DIR, 'setup_custom_project')
        with working_directory_keeper:
            os.chdir(addons_dir)
            keywords = prepare_odoo_addons()
            self.assertEquals(keywords, {
                'include_package_data': True,
                'install_requires': ['odoo>=8.0a,<9.0a',
                                     'python-dateutil'],
                'namespace_packages': ['odoo_addons'],
                'packages': ['odoo_addons'],
                'zip_safe': False,
            })


if __name__ == '__main__':
    unittest.main()