# -*- coding: utf-8 -*-
{
    'name': "Font IranSans EN",

    'summary': """
        It will show the jalaali date for most of date fields""",

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://gilaneh.com/shop/odoo-jalaali-date-1",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Tools/UI',
    'application': False,
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    'assets': {
        'web.assets_backend': [
            'gil_font_iransans_en/static/src/css/fonts.scss',
            'gil_font_iransans_en/static/src/css/fonts_web.scss',
            ],
        'web.assets_frontend': [
            'gil_font_iransans_en/static/src/css/fonts.scss',
            'gil_font_iransans_en/static/src/css/fonts_front.scss',
        ],
        'web.report_assets_common': [
            'gil_font_iransans_en/static/src/css/fonts.scss',
            'gil_font_iransans_en/static/src/css/fonts_report.scss',
            ],
        },
    'license': 'LGPL-3',
}
