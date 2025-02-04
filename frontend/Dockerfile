# frontend/Dockerfile

# Estágio de construção
FROM node:18 as build

WORKDIR /app

# Copia e instala dependências
COPY package*.json ./
RUN npm install

# Copia o código e faz o build
COPY . .
RUN npm run build

# ---

# Estágio de produção (Nginx)
FROM nginx:alpine

# Copia o build do estágio anterior
COPY --from=build /app/build /usr/share/nginx/html

# Copia configuração customizada do Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expõe a porta 80
EXPOSE 80

# Comando para iniciar o Nginx
CMD ["nginx", "-g", "daemon off;"]