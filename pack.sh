temp_dir="vim-dox-spell-0.1"
mkdir -p $temp_dir/c-files
cp doxygen.vim tagstospl.py $temp_dir
cp index-sample.xml tags-sample vimrc-sample $temp_dir
cp c-files/* $temp_dir/c-files
cp README $temp_dir
tar -cvvzf "vim-dox-spell-0.1.tar.gz" $temp_dir/*
