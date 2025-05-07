from ultralytics import YOLO

if __name__ == "__main__":
    model = YOLO("yolo12s.pt")
    # model = YOLO("runs/detect/train/weights/last.pt")
    model.train(
        data="datasets/data.yaml",
        epochs=50,
        batch=-1,
        imgsz=640,
        close_mosaic=0,
        amp=False,
    )
