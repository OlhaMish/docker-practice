# Software development lab 3

### Python

Go to python-app directory and build the image:

```bash 
docker build -t python-app:1.0 .
```

Run the container:

```bash 
docker run -p 8080:8080 python-app:1.0
```

### Golang

Go to go-app directory and build the image:

```bash 
docker build -t go-app:1.0 .
```
Run the container:

```bash 
docker run -p 8080:8080 go-app:1.0
```

### Rust

Go to rust-app directory and build the image:

```bash 
docker build -t rust-app:1.0 .
```
Run the container:

```bash 
docker run -p 8080:8080 rust-app:1.0
```
