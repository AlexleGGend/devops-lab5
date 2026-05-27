FROM maven:3.8.5-openjdk-17-slim

WORKDIR /app

COPY pom.xml .
COPY src/ ./src/

RUN mvn clean package -DskipTests
RUN cp /app/target/*.jar app.jar

CMD ["java", "-jar", "app.jar"]
