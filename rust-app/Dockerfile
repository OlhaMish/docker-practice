FROM rust:slim-bullseye AS builder

WORKDIR /app

COPY . .

RUN cargo install --locked --path .

RUN cargo build --release

FROM gcr.io/distroless/cc-debian11 AS final

COPY --from=builder /app/target/release/rust-app /app/rust-app

WORKDIR /app

EXPOSE 8080

CMD ["./rust-app"]