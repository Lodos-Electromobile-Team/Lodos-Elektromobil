#include "parkpilot.h"
#include "ui_park_pilot.h"

Park_Pilot::Park_Pilot(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Park_Pilot)
{
    ui->setupUi(this);
}

Park_Pilot::~Park_Pilot()
{
    delete ui;
}
