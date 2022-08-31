# Investigation into the correlation between AI in a simulated environment and using a real low-cost UAV
##### IRP-AAI-THESIS-HS 
 
1. [Aims and Objectives](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#aims-and-objectives)
   - [Aims](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#aims)
   - [Objectives](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#Objectives)
2. [Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
   - [Apple Real World Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#hugetextcolormaroontextbfapple---real-world)
   - [Apple Simulation Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#hugetextcolormaroontextbfapple---simulation)
   - [Banana Real World Results](#hugetextcoloryellowtextbfbanana---real-world)
   - [Banana Simulation Results](#hugetextcoloryellowtextbfbanana---simulation)
   - [Broccoli Real World Results](#hugetextcolorforestgreentextbfbroccoli---real-world)
   - [Broccoli Simulation Results](#hugetextcolorforestgreentextbfbroccoli---simulation)
   - [Tomato Real World Results](#hugetextcolorbrickredtextbftomato---real-world)
   - [Tomato Simulation Results](#hugetextcolorbrickredtextbftomato---simulation)
   - [Orange Real World Results](#hugetextcoloryelloworangetextbforange---real-world)
   - [Orange Simulation Results](#hugetextcoloryelloworangetextbforange---simulation)
   
## Aims and Objectives
### _**Aims:**_
The aim of this thesis is to gain an understanding through an
investigative experimentation the effectiveness of an object
detector under varying illumination conditions and altitudes on
its ability to classify and detect trained targets in a simulated
and real-world environment by using a camera sensor from a
UAV to determine if there are any differences.
### _**Objectives:**_
1. Devise an Experiment that is applicable in a simulation and the
real world that utilises key “object targets” that the UAV can
classify.
1. Accurately construct the Real-World experimental space
within the simulation environment.
2. Synthesise & Train an AI algorithm within the realm of
object detection using current methods.
3. Integrate the trained object detector algorithm into a UAV
within a simulated and real-world environment.
4. Conduct both experiments within the environments to
obtain valid results.
5. Evaluate results by comparing gathered data and establish
reasonings using evidence behind any differences or similarities.

## Tabulated Results 




### Key "N = Low/Medium/High"
`| Altitude (meters) | Class Label (N - Illuminance Level) | Prediction Confidience Percentage (N - Illuminance Level)|`


---
### $$\Huge\textcolor{Maroon}{\textbf{Apple - Real World}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    29.3   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    38.8   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    42.9   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    34.5   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    37.4   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    34.8   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    32.4   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$|    35.9   |$$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    34.0   |
|  **2.0**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    29.4   | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    34.6   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$|    35.5   |
|  **2.5**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    30.4   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    57.9   |$$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    39.0   |
|  **3.0**  | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    31.0   | $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    97.3   |$$\small\textcolor{yellowgreen}{\textbf{Apple}}$$ |    34.7   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
### $$\Huge\textcolor{Maroon}{\textbf{Apple - Simulation}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  |   $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$   |    44.2   |  $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    67.4   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    71.7   |
|  **1.0**  |   $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$   |    28.3   | $$\small\textcolor{salmon}{\textbf{Tomato}}$$  |    36.7   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    39.0   |
|  **1.5**  | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$  |    27.2   |  $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    33.0   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    37.8   |
|  **2.0**  | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$  |    27.1   |  $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    34.7   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    37.2   |
|  **2.5**  | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$  |    27.0   |  $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    28.1   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    36.9   |
|  **3.0**  |   $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$   |    28.8   | $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    51.1   | $$\small\textcolor{yellowgreen}{\textbf{Apple}}$$  |    36.9   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---

### $$\Huge\textcolor{yellow}{\textbf{Banana - Real World}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    37.7   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    49.5   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    41.2   |
|   **1.0**   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    33.6   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    35.9   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    38.0   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    31.4   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$|    38.7   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    34.9   |
|   **2.0**   |$$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    28.8   |$$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    36.3   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    34.3   |
|  **2.5**  | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    29.7   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    59.1   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    33.8   |
|   **3.0**   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    31.2   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    78.3   |   $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    35.4   |


[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
--- 
 ### $$\Huge\textcolor{yellow}{\textbf{Banana - Simulation}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  |  $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$  |    76.4   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    94.5   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$|    94.7   |
|   **1.0**   |  $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    31.5   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    29.7   |$$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    34.6   |
|  **1.5**  |  $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$  |    30.1   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$|    33.7   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    33.7   |
|   **2.0**   |  $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$  |    28.4   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    30.0   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    30.9   |
|  **2.5**  | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    28.1   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    27.5   | $$\small\textcolor{yellowgreen}{\textbf{Banana}}$$ |    34.3   |
|   **3.0**   | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    28.4   | $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    52.5   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    34.8   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 ### $$\Huge\textcolor{ForestGreen}{\textbf{Broccoli - Real World}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    29.1   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    89.3   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    87.6   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    29.5   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    49.1   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    51.3   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.3   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    35.7   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    35.4   |
|  **2.0**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.6   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.0   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.0   |
|  **2.5**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    31.0   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    94.8   |   $$\small\textcolor{salmon}{\textbf{Apple}}$$  |    37.2   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Tomato}}$$  |    31.2   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    96.0   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    33.9   |


[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 
 ### $$\Huge\textcolor{ForestGreen}{\textbf{Broccoli - Simulation}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    66.6   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    69.9   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    87.0   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.0   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    33.7   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    33.4   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    31.2   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    31.3   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    33.2   |
|  **2.0**  |  $$\small\textcolor{salmon}{\textbf{Tomato}}$$  |    30.0   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    28.9   | $$\small\textcolor{yellowgreen}{\textbf{Broccoli}}$$ |    32.2   |
|  **2.5**  |  $$\small\textcolor{salmon}{\textbf{Tomato}}$$  |    27.1   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    32.6   |   $$\small\textcolor{salmon}{\textbf{Apple}}$$  |    33.2   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Tomato}}$$  |    26.3   |  $$\small\textcolor{salmon}{\textbf{Orange}}$$  |    68.0   |   $$\small\textcolor{salmon}{\textbf{Apple}}$$  |    32.3   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 
 
 
 ### $$\Huge\textcolor{BrickRed}{\textbf{Tomato - Real World}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    45.6   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    48.6   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    46.6   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    43.3   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    43.8   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    34.2   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    40.7   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    38.3   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    35.9   |
|  **2.0**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    33.1   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    37.5   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    37.7   |
|  **2.5**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    28.1   | $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    52.6   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    37.4   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    30.2   | $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    88.1   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    37.1   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 ### $$\Huge\textcolor{BrickRed}{\textbf{Tomato - Simulation}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    34.7   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    47.8   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    41.9   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    30.4   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    40.2   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    35.9   |
|  **1.5**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    28.7   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    34.6   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    37.8   |
|  **2.0**  | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    28.4   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    33.7   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    37.2   |
|  **2.5**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    30.1   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    30.1   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    38.0   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    29.9   | $$\small\textcolor{salmon}{\textbf{Orange}}$$ |    49.6   | $$\small\textcolor{yellowgreen}{\textbf{Tomato}}$$ |    36.8   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 
 ### $$\Huge\textcolor{YellowOrange}{\textbf{Orange - Real World}}$$

|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    39.5   |   $$\small\textcolor{salmon}{\textbf{Apple}}$$  |    39.4   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    31.5   |
|  **1.0**  | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    39.7   | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    39.0   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    37.4   |
|  **1.5**  | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    36.0   | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    32.5   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    37.6   |
|  **2.0**  | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    36.9   | $$\small\textcolor{salmon}{\textbf{Broccoli}}$$ |    34.3   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    34.8   |
|  **2.5**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    29.7   |  $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$  |    73.2   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    33.0   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    30.7   |  $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$  |    98.6   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    34.4   |

[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 
 ### $$\Huge\textcolor{YellowOrange}{\textbf{Orange - Simulation}}$$
|Altitude (m) | Class (Low) | Confidence% (Low) | Class (Medium)  | Confidence% (Medium) | Label (High) | Confidence% (High)|
|:---------:|:------:|:----------:|:------:|:----------:|:------:|:----------:|
|  **0.5**  | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    52.8   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    66.7   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    54.7   |
|  **1.0**  | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    41.2   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    32.2   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    35.2   |
|  **1.5**  | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    30.3   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    31.8   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |   35.6   |
|  **2.0**  | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    28.6   | $$\small\textcolor{salmon}{\textbf{Tomato}}$$ |    31.2   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    36.4   |
|  **2.5**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    27.7   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    26.7   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    36.8   |
|  **3.0**  |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    28.2   | $$\small\textcolor{yellowgreen}{\textbf{Orange}}$$ |    63.9   |  $$\small\textcolor{salmon}{\textbf{Apple}}$$ |    36.3   |


[Back to Tabulated Results](https://github.com/Atrofos/IRP-AAI-THESIS-HS/blob/main/README.md#tabulated-results)
---
 
 
### Picture Results


