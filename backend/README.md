# Drinkapp Backend

*a.k.a. `drinkapi`*

### Running

1. Build the image
```bash
docker build -t drinkapi .
```

2. Run it on port 8000
```bash
docker run -p 8000:8000 -it drinkapi
```

### Quality Checks

Running `make all` will lint, typecheck, and test the code.
Each can instead be run individually, with `make lint`, `make typecheck`, and `make test` respectively.
