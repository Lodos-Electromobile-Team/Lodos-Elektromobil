#ifndef PARK_PILOT_H
#define PARK_PILOT_H

#include <QWidget>

namespace Ui {
class Park_Pilot;
}

class Park_Pilot : public QWidget
{
    Q_OBJECT

public:
    explicit Park_Pilot(QWidget *parent = nullptr);
    ~Park_Pilot();

private:
    Ui::Park_Pilot *ui;
};

#endif // PARK_PILOT_H
