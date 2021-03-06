try:
    import concurrent.futures as futures
except ImportError:
    try:
        import futures
    except ImportError:
        futures = None

import zipfile
import shutil
import tempfile
import requests

from os import path


#--- Globals ----------------------------------------------
PLUGINS = """
ack.vim https://github.com/mileszs/ack.vim
bufexplorer https://github.com/corntrace/bufexplorer
ctrlp.vim https://github.com/ctrlpvim/ctrlp.vim
nerdtree https://github.com/scrooloose/nerdtree
nginx-vim-syntax https://github.com/evanmiller/nginx-vim-syntax
open_file_under_cursor.vim https://github.com/amix/open_file_under_cursor.vim
vim-coffee-script https://github.com/kchmck/vim-coffee-script
vim-less https://github.com/groenewege/vim-less
vim-markdown https://github.com/tpope/vim-markdown
vim-surround https://github.com/tpope/vim-surround
vim-fugitive https://github.com/tpope/vim-fugitive
syntastic https://github.com/scrooloose/syntastic
vim-go https://github.com/fatih/vim-go
vim-gitgutter https://github.com/airblade/vim-gitgutter
gruvbox https://github.com/morhetz/gruvbox
vim-pug https://github.com/digitaltoad/vim-pug
vim-airline https://github.com/vim-airline/vim-airline
vim-airline-themes https://github.com/vim-airline/vim-airline-themes
vim-scala https://github.com/derekwyatt/vim-scala
vim-dues https://github.com/ajmwagar/vim-dues
vim-srcery-drk https://github.com/kudabux/vim-srcery-drk
vim-srcery https://github.com/roosta/vim-srcery
rainbow https://github.com/luochen1990/rainbow
vim-afterglow https://github.com/danilo-augusto/vim-afterglow
neocomplete.vim https://github.com/Shougo/neocomplete.vim
vim-better-whitespace https://github.com/ntpeters/vim-better-whitespace
nerdtree-git-plugin https://github.com/Xuyuanp/nerdtree-git-plugin
vim-crunchbang https://github.com/nightsense/vim-crunchbang
colbalt https://github.com/gkjgh/cobalt
vim-deep-space https://github.com/tyrannicaltoucan/vim-deep-space
vim-one https://github.com/rakr/vim-one
neodark https://github.com/KeitaNakamura/neodark.vim
vim-colors-solarized https://github.com/altercation/vim-colors-solarized
""".strip()

GITHUB_ZIP = '%s/archive/master.zip'

SOURCE_DIR = path.join(path.dirname(__file__), 'sources_non_forked')


def download_extract_replace(plugin_name, zip_path, temp_dir, source_dir):
    temp_zip_path = path.join(temp_dir, plugin_name)

    # Download and extract file in temp dir
    req = requests.get(zip_path)
    open(temp_zip_path, 'wb').write(req.content)

    zip_f = zipfile.ZipFile(temp_zip_path)
    zip_f.extractall(temp_dir)

    plugin_temp_path = path.join(temp_dir,
                                 path.join(temp_dir, '%s-master' % plugin_name))

    # Remove the current plugin and replace it with the extracted
    plugin_dest_path = path.join(source_dir, plugin_name)

    try:
        shutil.rmtree(plugin_dest_path)
    except OSError:
        pass

    shutil.move(plugin_temp_path, plugin_dest_path)

    print('Updated {0}'.format(plugin_name))


def update(plugin):
    name, github_url = plugin.split(' ')
    zip_path = GITHUB_ZIP % github_url
    download_extract_replace(name, zip_path,
                             temp_directory, SOURCE_DIR)


if __name__ == '__main__':
    temp_directory = tempfile.mkdtemp()

    try:
        if futures:
            with futures.ThreadPoolExecutor(16) as executor:
                executor.map(update, PLUGINS.splitlines())
        else:
            [update(x) for x in PLUGINS.splitlines()]
    finally:
        shutil.rmtree(temp_directory)
