# Face detector

![GitHub repo size](https://img.shields.io/github/repo-size/matheusassism/FaceDetectorDlib?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/matheusassism/FaceDetectorDlib?style=for-the-badge)

![image](https://user-images.githubusercontent.com/65235458/142041132-dd84157f-ad0e-43e1-bd8b-5699b7c6fead.png)


> Project in OPENCV for capture faces in a image (JEPG)

<!-- ## Improves and adjustments

The project is still under development and as updates will be focused on the following tasks:

- [ ] Can download the faces pictures
- [ ] Accept more images format
- [ ] Guess the age of faces -->

## General archtecture

> [All archtecture docs](https://drive.google.com/file/d/1JvW6XA4GrQAIhe1V5un09RYPUQAQW64C/view?usp=sharing)

<img src="https://user-images.githubusercontent.com/65235458/142350172-6d037e14-633b-4251-a4a9-d4160e1dec02.png" alt="diagram" width="700">

## 💻 Requirements

Before starting, make sure you meet the following requirements:

* Python 3.6 +
* Linux (Tested just on linux)
* [Dlib installed](https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/)

## 🚀 Installing on Linux

### (optional) Create a python venv:
```
python3 -m venv venv
source ./venv/bin/activate
```

### Install Libraries:

#### Server side

```
cd ./server
pip3 install -r requirements.txt
```
#### Client side

```
cd ./client
yarn
```

## ☕ Runing

### Running server:

```
cd ./server
uvicorn app.main:app
```

> After start you can acces the API swagger at http://127.0.0.1:8000/docs

### Running client:

```
cd ./client
yarn dev
```
> You can acces the client side at http://localhost:3000/

[⬆ Voltar ao topo](#nome-do-projeto)<br>
