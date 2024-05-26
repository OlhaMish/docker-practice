# Use the latest version of the Rust base image
FROM rust:latest

# Set the working directory in the container to /my
WORKDIR /usr/src/rust-app

# Copy the Rust project files to the working directory
COPY . .

# Build the Rust app
RUN cargo build --release

# Set the command to run the Rust app
CMD ["./target/release/rust-app"]

EXPOSE 8080