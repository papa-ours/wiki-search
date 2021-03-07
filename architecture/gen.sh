# {
    cd src

    if [ "$1" != "" ]; then
        mkdir ../diagrams/$1
        python -m plantuml $1/*.plantuml -o ../diagrams/
    else
        for f in *; do
            if [ -d "$f" ]; then
                mkdir ../diagrams/$f
                python -m plantuml $f/*.plantuml -o ../diagrams/
            fi
        done
    fi
# } &> /dev/null
cd ..
echo 'Generation complete'
