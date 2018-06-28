#!/usr/bin/env python3

# python setup.py sdist --format=zip,gztar

import argparse
import imp
import os
import platform
import sys
from setuptools import setup

with open('./requirements.txt') as f:
    requirements = f.read().splitlines()

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (3, 4, 0):
    sys.exit("Error: Electrum requires Python version >= 3.4.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root=', dest='root_path', metavar='dir', default='/')
    opts, _ = parser.parse_known_args(sys.argv[1:])
    usr_share = os.path.join(sys.prefix, "share")
    icons_dirname = 'pixmaps'
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        icons_dirname = 'icons'
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['btn-electrum.desktop']),
        (os.path.join(usr_share, icons_dirname), ['icons/electrum.png'])
    ]

setup(
    name="Btn Electrum",
    version=version.ELECTRUM_VERSION,
    install_requires=requirements,
    packages=[
        'btn_electrum',
        'btn_electrum_gui',
        'btn_electrum_gui.qt',
        'btn_electrum_plugins',
        'btn_electrum_plugins.audio_modem',
        'btn_electrum_plugins.email_requests',
        'btn_electrum_plugins.greenaddress_instant',
        'btn_electrum_plugins.hw_wallet',
        'btn_electrum_plugins.labels',
        'btn_electrum_plugins.ledger',
        'btn_electrum_plugins.trezor',
        'btn_electrum_plugins.digitalbitbox',
        'btn_electrum_plugins.trustedcoin',
        'btn_electrum_plugins.virtualkeyboard',
    ],
    package_dir={
        'btn_electrum': 'lib',
        'btn_electrum_gui': 'gui',
        'btn_electrum_plugins': 'plugins',
    },
    package_data={
        'btn_electrum': [
            'currencies.json',
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
            'servers.json',
            'servers_testnet.json',
        ]
    },
    scripts=['btn-electrum'],
    data_files=data_files,
    description="Lightweight Btn Wallet",
    author="CodeFace",
    author_email="codeface@btn.org",
    license="MIT Licence",
    url="https://btn.org",
    long_description="""Lightweight Btn Wallet"""
)
