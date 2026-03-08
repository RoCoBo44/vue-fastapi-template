FROM oven/bun:latest

WORKDIR /app

# Copy package management
COPY package.json ./

# Install dependencies using bun
RUN bun install

# Copy application files
COPY . .

# Expose Vite dev server port
EXPOSE 5173

# Run the frontend
CMD ["bun", "run", "dev"]
