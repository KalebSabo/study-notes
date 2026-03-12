# Electrical Notes
- This file will focus on the circuit board/electronic research

## Electricity
- Arises from the presence, motion and interactions of electric charges. Attraction/Repulsion.
- A low-entropy form of energy
- non-equilibrium thermodynamics
- Governed by Ohm's Law
    - $V = I*R$
    - #### Voltage
        - $V$ = Voltage (Potential Difference/Tension/Pressure in charge)
            - The build up of electric charge
                - Electron Elementary charge ($e$) = $-1.602*10^{-19}$
            - A physical scalar quantity
            - The source, loss, dissipation, or storage of energy
            - Higher Voltage -> Lower Voltage
    - #### Current
        - $I$ = Current/Amperage (How many electrons/Coulombs passing at a point per second)
            - Amperage/Amp(s) = base SI unit (see above)
            - "Net rate of flow of electric charge through a surface"
                - Electron/Proton are equal in magnitude? but opposite signs
                    - hence, electrically neutral atoms when equivalent electrons/protons
            - $1A = 1C/s = \frac{1}{1.602*10^{-19}}$ e/s = $\frac{10^{19}*e}{1.602s}$
            - 1 Amp = 1 Coulomb per second
            - Quarks etc. (Out of scope for Eragon)
    - #### Resistance/Conductance
        - $R$ = Resistance (Difficulty in electrons to pass/friction)
            - A measure of the opposition to the flow of electrons
                - Can be measured on the **difficulty** or **ease** of electron passage (based on frame of reference)
            - Electrical Resistance (Ohms $\Omega$) or Conductance (Siemans $S$)
            - Resistance is dependant on material
                - All objects are conductors
                    - Ease of valence electron or ion movement determines if it is a good Conductor/Insulator
        - ##### Temperature
            - Influences motion of atoms/electrons, thus affects resistance
                - Resistance $R = R_0(1 + \alpha(T - T_0))$
                    - $R_0$ = Base Resistance at reference $T_0$
                    - $\alpha$ = Temp Coefficient, material specific
                        - how much resistance changes per degree of temp change for the specific material
                        - Copper $\alpha$ = 0.00393/$\degree C$
                - Temp sensors take advantage of this! (see Thermisistors)
                - Limitations of equation
                    - Extreme Temps need more precise measurements, as the linearity of the resistance change is assumed!
                    - Superconductors are different
                    - Impurities/Strain/Magnetic fields can alter $\alpha$


### Electrical Wires

- #### Wire Resistance
    - Resistance $R = \rho \frac{L}{A}$
        - $\rho$ = Resistivity of material (look at material properties)
            - i.e. Silver $\rho = 1.59 * 10^-8 \Omega * m$
        - $L$ = Length of wire (Electron Collisions)  
        - $A$ = Cross-sectional area of the wire (Freedom of movement)

- #### Current Density
    - Measure of how many amps is passing in a particular area of a wire
    - Current density can explain heating/efficiency/safety issues
    - high density = overheating, low density = smooth flow
        - Current Density $J = \frac{I}{A}$
            - Current Density $J$ in Amperes/$m^2$
            - $I$ = Total Current flowing in wire (Amps)
            - $A$ = Cross-sectional area of the wire
    - Typically $\vec{J}$ But were assuming a straight wire! Only need the scalar value 

## Semiconductor
- Material with electrical conductivity between that of a conductor and an insulator
    - Conductivity is modified by adding impurites to it's structure
        - aka **Doping**
    - ##### **Dies (i.e. silicon die)** 
        - a small thin slice/block (i.e. silicon) on which an entire integrated circuit is fabricated
        - can hold things like the microprocessor/memory chip

## Data
- Values or Information
    - There are differing types
        - Raw Data
            - unprocessed
        - Structured Data
            - JSON files, organized notes like this one
        - Processed Data
            - Data that has gone through a process (like an algorithm) and created an output

## Analog
- type of signal or system that represents data as continuous, varying physical quantities
    - like voltage, current or sound waves

## Digital
- 

## Transistor
- 

## Resistor
- 




## Breadboard
- Plastic board with holes connected by metal clips
    - **Terminal Strips**
        - Horizontal rows (from letters A-J)
            - Each row connects horizontally, allowing up to 5 component to share a connection. 
    - **Central Ravine**
        - The 'ditch' between the two sides of the board
            - separates electrically
    - **Power Rails**
        - Vertical columns along the edges
            - Often marked with a red positive/black or blue negative sign

## Arduino Uno R3
- Currently TBA for Eragon

## ESP32
- ESP32 System-on-Chip (SoC)
    - Combines multiple components
        - i.e. CPU, memory, peripherals
    - Placed on a single silicone die
!['See ESP32_Components Image for a great breakdown'](../05_Images/ESP32_Components.webp)
    - **IO Pins**
        - 30-38 pins
            - **Be careful!!** some pins are specific
!['See IOpinDiagram.png inside Images folder for a great visual](../05_Images/IOpinDiagram.png)
        - Acronyms
            - ADC = Analog-to-Digital Converter
            - CP2102 = Chip Model from Silicon Labs
            - DAC = Digital-to-Analog Convertor
            - EN = Enable

