package uz.mq.mybaby;

public class RequestModel {
    String action;
    String fileName;

    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String fileName) {
        this.fileName = fileName;
    }

    public RequestModel(String action, String fileName) {
        this.action = action;
        this.fileName = fileName;
    }
}
