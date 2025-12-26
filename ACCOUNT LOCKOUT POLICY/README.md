# Account Lockout Policy Simulation (Python)

### 🛡️ Objective
This project simulates a fundamental security control: the **Account Lockout Policy**. It implements a mechanism that monitors login attempts and disables access after a predefined threshold of failures, effectively mitigating automated brute-force attacks.

### 🛠️ Technical Implementation
* **Language:** Python
* **Control Flow:** Nested `while` loops for continuous user validation and credential checking.
* **Logic:** * `intentos_restantes`: A dynamic counter to track remaining attempts.
    * `exit()`: Immediate termination of the session upon security violation.

### 🔍 Code Highlights & Logic
This script processes security access in two distinct phases:
1. **User Identification:** The script ensures the user exists before prompting for a password.
2. **Credential Validation:**
   ```python
   while intentos_restantes > 0:
       # Calculates the current attempt number for transparency
       intentos_actuales = max_intentos - intentos_restantes + 1
       # If the password fails 3 times, the system triggers a lockout
       if entrada_contraseña != contraseña_correcta:
           intentos_restantes -= 1

3. **Session Hardening:¨¨ Once intentos_restantes reaches zero, the exit() function prevents any further interaction, simulating a blocked account status.

### ⚠️ Cybersecurity Significance
In a real-world environment, this policy is critical because:

- Brute-Force Protection: It prevents attackers from using automated scripts to guess thousands of password combinations.

- Risk Mitigation: It reduces the attack surface by limiting the time and attempts an unauthorized user has to gain access.

- Incident Detection: Frequent lockouts can serve as an Indicator of Compromise (IoC), alerting security teams to potential targeted attacks
