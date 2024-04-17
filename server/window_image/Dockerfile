# Use the base Windows Server Core image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Metadata indicating an image maintainer
LABEL maintainer="Your Name <your.email@example.com>"

# Set environment variables (if needed)
ENV APP_HOME=C:\\app

# Create app directory
RUN mkdir %APP_HOME%

# Set the working directory
WORKDIR %APP_HOME%

# Copy files from host to container
COPY . %APP_HOME%

# Example: Install dependencies (modify as needed)
RUN ["powershell", "Install-PackageProvider -Name NuGet -Force -Verbose -Scope AllUsers"]

# Example: Run any necessary commands (modify as needed)
RUN ["powershell", "Install-Module -Name Az -AllowClobber -Scope AllUsers -Force"]

# Example: Expose a port (modify as needed)
EXPOSE 80

# Example: Start the application (modify as needed)
CMD ["powershell", "Start-Service -Name w3svc"]
