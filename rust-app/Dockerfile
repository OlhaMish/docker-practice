FROM rust:1.77.0-slim as builder

COPY . /app

WORKDIR /app

RUN cargo build --release

FROM debian:bullseye-slim AS final

COPY --from=builder /app/target/release/rust-app /app/rust-app
WORKDIR /rust-app

CMD ["./rust-app"]

EXPOSE 8080
