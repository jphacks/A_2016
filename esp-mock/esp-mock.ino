/*
  JPHacks2020
  team a_2016
  mock device
*/

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "takapiro2";
const char* password = "2kumifriends";

const char* serverURL = "https://a-2016-backend.herokuapp.com/devices/weight";
//const char* serverURL = "https://jsonplaceholder.typicode.com/posts";

const int sensorPin = 34;
const int yellowPin = 19;
const int orangePin = 18;
int sensorValue = 0;
// timer
unsigned long lastTime = 0;
const unsigned long timerDelay = 1000 * 1; // one second

char* device_ids[]={
  "ab568461",  "b8f6bc5d",
  "dde4ff89",  "e5181503"
};

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(sensorPin, ANALOG);
  pinMode(yellowPin, INPUT_PULLUP);
  pinMode(orangePin, INPUT_PULLUP);
  Serial.begin(115200);
  setup_wifi();
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    int yellow = digitalRead(yellowPin);
    int orange = digitalRead(orangePin);
    int type = 0;
    if (yellow && orange) {
      type = 3;
    } else if (yellow && !orange) {
      type = 2;
    } else if (!yellow && orange) {
      type = 1;
    }
    int weight = get_weight(type);
    send_data(device_ids[type], weight);
    lastTime = millis();
  }
}

int get_weight(int type) {
  sensorValue = analogRead(sensorPin);
  int value = 0;
  switch (type) {
    case 3:
      value = sensorValue / 4095 * 2000;
      break;
    case 2:
      value = sensorValue / 4095 * 1040;
      break;
    case 1:
      value = sensorValue / 4095 * 500;
      break;
    case 0:
      value = sensorValue / 4095 * 300;
      break;
  }
  if (value < 20) {
    return 0;
  }
  return value;
}

void send_data(String device_id, int weight) {
  if (WiFi.status() == WL_CONNECTED) {
    digitalWrite(LED_BUILTIN, HIGH);
    HTTPClient http;
    http.begin(serverURL);
    http.addHeader("Content-Type", "application/json");
    String httpRequestData = "{\"device_id\": \"" + device_id + "\",\"weight\":" + String(weight) + "}";
    int httpResponseCode = http.PUT(httpRequestData);
    String res = http.getString();
    Serial.println("req body: " + httpRequestData);
    Serial.println("response: " + res);
    http.end();
    Serial.print("status code: ");
    Serial.println(httpResponseCode);
  } else {
    Serial.println("no wifi");
    digitalWrite(LED_BUILTIN, HIGH);
    delay(300);
    digitalWrite(LED_BUILTIN, LOW);
    delay(300);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(300);
  }
  digitalWrite(LED_BUILTIN, LOW);
}

void setup_wifi() {
  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
