pyrcc5 icons.qrc -o gui/qt/icons_rc.py
protoc --proto_path=lib/ --python_out=lib/ lib/paymentrequest.proto
