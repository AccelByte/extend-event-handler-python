FROM python:3.10-slim
WORKDIR /data
RUN apt update \
        && apt install -y bash curl git jq make xxd \
        && apt clean \
        && rm -rf /var/lib/apt/lists/*
RUN ARCH=$(uname -m | sed -e s/aarch64/arm64/) \
        && curl -sSL "https://github.com/fullstorydev/grpcurl/releases/download/v1.8.9/grpcurl_1.8.9_linux_$ARCH.tar.gz" | tar -xz -C /usr/local/bin
RUN ARCH=$(uname -m | sed -e s/x86_64/amd64/ -e s/aarch64/arm64/) \
        && curl "https://download.docker.com/linux/debian/dists/bookworm/pool/stable/$ARCH/docker-ce-cli_23.0.6-1~debian.12~bookworm_$ARCH.deb" -o /tmp/docker-ce-cli.deb \
        && curl "https://download.docker.com/linux/debian/dists/bookworm/pool/stable/$ARCH/docker-buildx-plugin_0.11.2-1~debian.12~bookworm_$ARCH.deb" -o /tmp/docker-buildx-plugin.deb \
        && cat /tmp/docker-ce-cli.deb \
        && dpkg -i /tmp/docker-ce-cli.deb /tmp/docker-buildx-plugin.deb \
        && rm -f /tmp/docker-ce-cli.deb /tmp/docker-buildx-plugin.deb
COPY --from=ngrok/ngrok /bin/ngrok /bin/ngrok