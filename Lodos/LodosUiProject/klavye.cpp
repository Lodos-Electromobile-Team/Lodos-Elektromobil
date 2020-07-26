#include "klavye.h"
#include "ui_klavye.h"

klavye::klavye(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::klavye)
{
    ui->setupUi(this);
}

klavye::~klavye()
{
    delete ui;
}
