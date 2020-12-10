class Canvas {
    constructor(canvasW, canvasH) {
        this.w = canvasW;
        this.h = canvasH;
    }
    setSize() {
        $('#layout').css({'width':this.w,'height':this.h})
    }
    getSize() {
        return `${this.w}, ${this.h}`
    }
}