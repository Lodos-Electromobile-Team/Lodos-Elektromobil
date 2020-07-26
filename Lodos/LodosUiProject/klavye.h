#ifndef KLAVYE_H
#define KLAVYE_H

#include <QWidget>

namespace Ui {
class klavye;
}

class klavye : public QWidget
{
    Q_OBJECT

public:
    explicit klavye(QWidget *parent = nullptr);
    ~klavye();

private:
    Ui::klavye *ui;
};

#endif // KLAVYE_H
