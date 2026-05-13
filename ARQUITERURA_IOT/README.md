# 🌐 Arquitetura de IoT (Internet das Coisas)

## 📑 1. Conteúdo de Aula
*   **Conceito de IoT:** Extensão da conectividade da internet para objetos físicos do cotidiano através de sensores e atuadores.
*   **Pilares Fundamentais:** Identificação de dispositivos, coleta de dados, processamento distribuído e segurança da informação.
*   **Desafios Técnicos:** Restrição de energia (baterias), latência de rede, largura de banda e interoperabilidade entre sistemas distintos.

---

## 🏗️ 2. Arquitetura em Camadas
*   **Camada de Percepção (Física):** Dispositivos de hardware, microcontroladores, sensores (capturam dados do ambiente) e atuadores (executam ações físicas).
*   **Camada de Rede (Conectividade):** Protocolos de transmissão de dados e gateways que conectam a camada física aos servidores de nuvem.
*   **Camada de Aplicação:** Plataformas de visualização de dados, dashboards, inteligência artificial e interfaces para o usuário final.

---

## 🔌 3. Hardware e Dispositivos IoT
*   **Microcontroladores Comuns:**
    *   **Arduino:** Excelente para prototipagem rápida e projetos de baixa complexidade.
    *   **ESP32 / ESP8266:** Módulos com Wi-Fi e Bluetooth integrados nativamente, ideais para projetos de IoT conectados.
    *   **Raspberry Pi:** Computador de placa única com sistema operacional (Linux), usado para tarefas pesadas de Edge Computing.
*   **Sensores vs. Atuadores:**
    *   **Sensores:** DHT11 (temperatura/umidade), LDR (luminosidade), Ultrassônico (distância).
    *   **Atuadores:** Relés (controle de lâmpadas/motores), Servomotores, Buzzers (avisos sonoros).

---

## 📡 4. Protocolos de Comunicação e Rede
*   **Protocolos de Aplicação (M2M):**
    *   **MQTT:** Baseado em arquitetura Publicador/Assinante (Publish/Subscribe), extremamente leve e ideal para redes instáveis.
    *   **CoAP:** Protocolo web focado em restrição de recursos, similar ao HTTP mas rodando sobre UDP.
    *   **HTTP/REST:** Usado principalmente para integração entre gateways de IoT e APIs na nuvem.
*   **Tecnologias de Conectividade:**
    *   **Curto Alcance:** Wi-Fi, Bluetooth Low Energy (BLE), Zigbee.
    *   **Longo Alcance (LPWAN):** LoRaWAN, NB-IoT, Sigfox (baixo consumo de energia para longas distâncias).

---

## ☁️ 5. Edge Computing vs. Cloud Computing
*   **Edge Computing (Computação de Borda):**
    *   Processamento de dados realizado próximo à fonte (no próprio dispositivo ou gateway).
    *   **Vantagens:** Redução drástica da latência e economia no consumo de banda de rede.
*   **Cloud Computing (Computação em Nuvem):**
    *   Envio de dados consolidados para servidores centrais (AWS IoT Core, Azure IoT Central, Google Cloud IoT).
    *   **Vantagens:** Capacidade massiva de armazenamento, análise de Big Data e treinamento de modelos de IA.
