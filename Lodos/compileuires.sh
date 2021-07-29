#!/bin/bash
for i in LodosUiProject/*.ui; do
    filepath=${i/.ui/.py}
    name=$(basename "$filepath")
    pyuic5 -x $i -o $filepath

    cp $filepath ui/$name
    rm $filepath
done
pyrcc5 LodosUiProject/res.qrc -o ui/res_rc.py
pyrcc5 LodosUiProject/main.qrc -o ui/main_rc.py
pyrcc5 LodosUiProject/parkpilot.qrc -o ui/parkpilot_rc.py