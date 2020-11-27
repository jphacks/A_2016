#include "HX711.h"

// HX711 circuit wiring

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "takapiro2";
const char* password = "2kumifriends";

const char* serverURL = "https://a-2016-backend.herokuapp.com/devices/weight";
//const char* serverURL = "https://jsonplaceholder.typicode.com/posts";

long sensorValue = 0;
// timer
unsigned long lastTime = 0;
const unsigned long timerDelay = 1000 * 1; // one second

const String device_id = "2FFB458E";
const int LOADCELL_DOUT_PIN = 32;
const int LOADCELL_SCK_PIN = 33;

HX711 scale;

void setup() {;
  Serial.begin(115200);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
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
    sensorValue = scale.read_average(10);
    long A=411790.393;
    long B=108114.4105;
  int convertedValue = int((float(sensorValue)-float(B))/float(A)*1000);//mL
  if (convertedValue < 50) {
    return 0;
  }
  return convertedValue;
}

void send_data(int weight) {
  if (WiFi.status() == WL_CONNECTED) {
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
    delay(300);
    delay(300);
    delay(300);
  }
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
