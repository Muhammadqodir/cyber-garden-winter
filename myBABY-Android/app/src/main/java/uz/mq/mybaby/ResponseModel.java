package uz.mq.mybaby;

public class ResponseModel {
    int accuracy;
    int result;

    public int getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(int accuracy) {
        this.accuracy = accuracy;
    }

    public int getResult() {
        return result;
    }

    public void setResult(int result) {
        this.result = result;
    }

    public ResponseModel(int accuracy, int result) {
        this.accuracy = accuracy;
        this.result = result;
    }
}
