/*
  JPHacks2020
  team a_2016
*/

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "takapiro2";
const char* password = "2kumifriends";

const char* serverURL = "https://a-2016-backend.herokuapp.com/devices/weight";
//const char* serverURL = "https://jsonplaceholder.typicode.com/posts";

const int sensorPin = 34;
int sensorValue = 0;
// timer
unsigned long lastTime = 0;
const unsigned long timerDelay = 1000 * 1; // one second

const String device_id = "5CDCD561";

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(sensorPin, ANALOG);
  Serial.begin(115200);
  setup_wifi();
}

void loop() {
  if ((millis() - lastTime) > timerDelay) {
    int weight = get_weight();
    send_data(weight);
    lastTime = millis();
  }
}

int get_weight() {
  sensorValue = analogRead(sensorPin);
  int convertedValue = 1.39 * sensorValue - 728;
  if (convertedValue < 20) {
    return 0;
  }
  return convertedValue;
}

void send_data(int weight) {
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
