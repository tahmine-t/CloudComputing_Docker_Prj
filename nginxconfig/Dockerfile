# Use the official Nginx image from the Docker Hub
FROM nginx:latest

# Copy your Nginx configuration file from the host to the container
COPY ./webprj.conf /etc/nginx/conf.d/webprj.conf

# Copy all files from the ./frontend directory to /var/www/html/prj in the container
COPY ../frontend /var/www/html/prj

# Expose port 80 to the host
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
