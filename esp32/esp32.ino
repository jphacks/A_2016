/*
  JPHacks2020
  team a_2016
*/

#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "takapiro2";
const char* password = "2kumifriends";

//const char* serverURL = "https://a-2016-backend.herokuapp.com/states";
const char* serverURL = "https://jsonplaceholder.typicode.com/posts";

// timer
unsigned long lastTime = 0;
unsigned long timerDelay = 1000 * 10; // ten seconds

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
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
  return 100;
}

void send_data(int weight) {
  if (WiFi.status() == WL_CONNECTED) {
    digitalWrite(LED_BUILTIN, HIGH);
    HTTPClient http;
    http.begin(serverURL);
    // Specify content-type header
    http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    // Data to send with HTTP POST
    String httpRequestData = "device_id=5CDCD567&weight=500";
    // Send HTTP POST request
    int httpResponseCode = http.POST(httpRequestData);
    http.end();
    Serial.print("Weight was... ");
    Serial.println(weight);
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
