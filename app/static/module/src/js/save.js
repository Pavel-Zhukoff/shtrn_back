document.getElementById('save').addEventListener('click', function () {
    let pdf = new jsPDF('l', 'px', [stage.width(), stage.height()]);
    pdf.setTextColor('#000000');
    stage.find('Text').forEach((text) => {
        const size = text.fontSize() / 0.75;
        pdf.setFontSize(size);
        pdf.text(text.text(), text.x(), text.y(), {
            baseline: 'top',
            angle: -text.getAbsoluteRotation(),
        });
    });

    pdf.addImage(
        stage.toDataURL({ pixelRatio: 2 }),
        0,
        0,
        stage.width(),
        stage.height()
    );

    pdf.save('lesson.pdf');
});