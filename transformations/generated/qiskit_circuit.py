import sys
import os
sys.path = [p.strip() for p in sys.path if p]
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.circuit import Instruction

from qiskit_aer import AerSimulator

from qiskit.circuit.library import *
from qiskit.circuit.library.standard_gates import GlobalPhaseGate
import numpy as np










# Function Gate Definitions



# Initialize Registers

q = QuantumRegister(19, 'q')


c = ClassicalRegister(19, 'c')


# Initialize Circuit
qc = QuantumCircuit(q, c)

# Operations

qc.append(HGate(), [q[0]])

qc.append(HGate(), [q[1]])

qc.append(HGate(), [q[2]])

qc.append(HGate(), [q[3]])

qc.append(HGate(), [q[4]])

qc.append(HGate(), [q[5]])

qc.append(HGate(), [q[6]])

qc.append(HGate(), [q[7]])

qc.append(HGate(), [q[8]])

qc.append(HGate(), [q[9]])

qc.append(HGate(), [q[10]])

qc.append(HGate(), [q[11]])

qc.append(HGate(), [q[12]])

qc.append(HGate(), [q[13]])

qc.append(HGate(), [q[14]])

qc.append(HGate(), [q[15]])

qc.append(HGate(), [q[16]])

qc.append(HGate(), [q[17]])

qc.append(HGate(), [q[18]])

qc.append(RZGate(-0.33746822460783515), [q[0]])

qc.append(RZGate(-0.06135891367428855), [q[1]])

qc.append(RZGate(-0.2883836205054442), [q[2]])

qc.append(RZGate(-0.030677073028616098), [q[3]])

qc.append(RZGate(-0.024541865019631987), [q[4]])

qc.append(RZGate(-0.3067904364366606), [q[5]])

qc.append(RZGate(-0.04908102838959869), [q[6]])

qc.append(RZGate(-0.37428638570647155), [q[7]])

qc.append(RZGate(-0.5215483029626403), [q[8]])

qc.append(RZGate(-0.5338216590111267), [q[9]])

qc.append(RZGate(-0.006135923151542565), [q[10]])

qc.append(RZGate(-0.01227184630308513), [q[11]])

qc.append(RZGate(-0.02454369260617026), [q[12]])

qc.append(RZGate(-0.04908738521234052), [q[13]])

qc.append(RZGate(-0.09817477042468103), [q[14]])

qc.append(RZGate(-0.19634954084936207), [q[15]])

qc.append(RZGate(-0.39269908169872414), [q[16]])

qc.append(RZGate(-0.7853981633974483), [q[17]])

qc.append(RZGate(-0.0859029241215959), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[1]])

qc.append(RZGate(0.023599704429009865), [q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[1]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[2]])

qc.append(RZGate(0.11091861081634635), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[3]])

qc.append(RZGate(0.011799852214504932), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[4]])

qc.append(RZGate(0.009439881771603945), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[5]])

qc.append(RZGate(0.11799852214504931), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[6]])

qc.append(RZGate(0.01887976354320789), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[7]])

qc.append(RZGate(0.14395819701696017), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[8]])

qc.append(RZGate(0.20059748764658386), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(RZGate(0.20531742853238583), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[10]])

qc.append(RZGate(0.002359970442900986), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[11]])

qc.append(RZGate(0.004719940885801972), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[12]])

qc.append(RZGate(0.009439881771603945), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[13]])

qc.append(RZGate(0.01887976354320789), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[14]])

qc.append(RZGate(0.03775952708641578), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[15]])

qc.append(RZGate(0.07551905417283156), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[16]])

qc.append(RZGate(0.1510381083456631), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[17]])

qc.append(RZGate(0.3020762166913262), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[18]])

qc.append(RZGate(0.033039586200613806), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[0], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[2]])

qc.append(RZGate(0.020167020148426612), [q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[2]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[3]])

qc.append(RZGate(0.002145427675364533), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[4]])

qc.append(RZGate(0.0017163421402916267), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[5]])

qc.append(RZGate(0.02145427675364533), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[6]])

qc.append(RZGate(0.0034326842805832533), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[7]])

qc.append(RZGate(0.026174217639447304), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[8]])

qc.append(RZGate(0.03647227048119706), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(RZGate(0.03733044155134287), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[10]])

qc.append(RZGate(0.00042908553507290667), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[11]])

qc.append(RZGate(0.0008581710701458133), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[12]])

qc.append(RZGate(0.0017163421402916267), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[13]])

qc.append(RZGate(0.0034326842805832533), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[14]])

qc.append(RZGate(0.006865368561166507), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[15]])

qc.append(RZGate(0.013730737122333013), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[16]])

qc.append(RZGate(0.027461474244666027), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[17]])

qc.append(RZGate(0.05492294848933205), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[18]])

qc.append(RZGate(0.0060071974910206926), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[1], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[3]])

qc.append(RZGate(0.010083510074213306), [q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[3]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[4]])

qc.append(RZGate(0.008066808059370644), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[5]])

qc.append(RZGate(0.10083510074213306), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[6]])

qc.append(RZGate(0.016133616118741288), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[7]])

qc.append(RZGate(0.12301882290540234), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[8]])

qc.append(RZGate(0.17141967126162622), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(RZGate(0.17545307529131152), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[10]])

qc.append(RZGate(0.002016702014842661), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[11]])

qc.append(RZGate(0.004033404029685322), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[12]])

qc.append(RZGate(0.008066808059370644), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[13]])

qc.append(RZGate(0.016133616118741288), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[14]])

qc.append(RZGate(0.032267232237482575), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[15]])

qc.append(RZGate(0.06453446447496515), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[16]])

qc.append(RZGate(0.1290689289499303), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[17]])

qc.append(RZGate(0.2581378578998606), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[18]])

qc.append(RZGate(0.028233828207797258), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[2], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[4]])

qc.append(RZGate(0.0008581710701458133), [q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[4]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[5]])

qc.append(RZGate(0.010727138376822666), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[6]])

qc.append(RZGate(0.0017163421402916267), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[7]])

qc.append(RZGate(0.013087108819723652), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[8]])

qc.append(RZGate(0.01823613524059853), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(RZGate(0.018665220775671437), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[10]])

qc.append(RZGate(0.00021454276753645333), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[11]])

qc.append(RZGate(0.00042908553507290667), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[12]])

qc.append(RZGate(0.0008581710701458133), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[13]])

qc.append(RZGate(0.0017163421402916267), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[14]])

qc.append(RZGate(0.0034326842805832533), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[15]])

qc.append(RZGate(0.006865368561166507), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[16]])

qc.append(RZGate(0.013730737122333013), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[17]])

qc.append(RZGate(0.027461474244666027), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[18]])

qc.append(RZGate(0.0030035987455103463), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[3], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(RZGate(0.008581710701458132), [q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[5]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(RZGate(0.001373073712233301), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[7]])

qc.append(RZGate(0.010469687055778922), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[8]])

qc.append(RZGate(0.014588908192478824), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(RZGate(0.01493217662053715), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[10]])

qc.append(RZGate(0.00017163421402916263), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[11]])

qc.append(RZGate(0.00034326842805832526), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[12]])

qc.append(RZGate(0.0006865368561166505), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[13]])

qc.append(RZGate(0.001373073712233301), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[14]])

qc.append(RZGate(0.002746147424466602), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[15]])

qc.append(RZGate(0.005492294848933204), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[16]])

qc.append(RZGate(0.010984589697866408), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[17]])

qc.append(RZGate(0.021969179395732816), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[18]])

qc.append(RZGate(0.002402878996408277), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[4], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(RZGate(0.017163421402916264), [q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[6]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[7]])

qc.append(RZGate(0.13087108819723653), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[8]])

qc.append(RZGate(0.1823613524059853), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(RZGate(0.18665220775671437), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[10]])

qc.append(RZGate(0.002145427675364533), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[11]])

qc.append(RZGate(0.004290855350729066), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[12]])

qc.append(RZGate(0.008581710701458132), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[13]])

qc.append(RZGate(0.017163421402916264), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[14]])

qc.append(RZGate(0.03432684280583253), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[15]])

qc.append(RZGate(0.06865368561166506), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[16]])

qc.append(RZGate(0.13730737122333012), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[17]])

qc.append(RZGate(0.27461474244666023), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[18]])

qc.append(RZGate(0.030035987455103462), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[5], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[7]])

qc.append(RZGate(0.020939374111557843), [q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[7]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[8]])

qc.append(RZGate(0.029177816384957648), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(RZGate(0.0298643532410743), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[10]])

qc.append(RZGate(0.00034326842805832526), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[11]])

qc.append(RZGate(0.0006865368561166505), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[12]])

qc.append(RZGate(0.001373073712233301), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[13]])

qc.append(RZGate(0.002746147424466602), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[14]])

qc.append(RZGate(0.005492294848933204), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[15]])

qc.append(RZGate(0.010984589697866408), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[16]])

qc.append(RZGate(0.021969179395732816), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[17]])

qc.append(RZGate(0.04393835879146563), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[18]])

qc.append(RZGate(0.004805757992816554), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[6], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[8]])

qc.append(RZGate(0.2224808499353021), [q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[8]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(RZGate(0.22771569346319157), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[10]])

qc.append(RZGate(0.0026174217639447304), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[11]])

qc.append(RZGate(0.005234843527889461), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[12]])

qc.append(RZGate(0.010469687055778922), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[13]])

qc.append(RZGate(0.020939374111557843), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[14]])

qc.append(RZGate(0.041878748223115686), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[15]])

qc.append(RZGate(0.08375749644623137), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[16]])

qc.append(RZGate(0.16751499289246274), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[17]])

qc.append(RZGate(0.3350299857849255), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[18]])

qc.append(RZGate(0.03664390469522623), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[7], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(RZGate(0.31730875318641444), [q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[9]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[10]])

qc.append(RZGate(0.003647227048119706), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[11]])

qc.append(RZGate(0.007294454096239412), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[12]])

qc.append(RZGate(0.014588908192478824), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[13]])

qc.append(RZGate(0.029177816384957648), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[14]])

qc.append(RZGate(0.058355632769915296), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[15]])

qc.append(RZGate(0.11671126553983059), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[16]])

qc.append(RZGate(0.23342253107966118), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[17]])

qc.append(RZGate(0.46684506215932237), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[18]])

qc.append(RZGate(0.051061178673675885), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[8], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[10]])

qc.append(RZGate(0.0037330441551342874), [q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[10]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[11]])

qc.append(RZGate(0.007466088310268575), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[12]])

qc.append(RZGate(0.01493217662053715), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[13]])

qc.append(RZGate(0.0298643532410743), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[14]])

qc.append(RZGate(0.0597287064821486), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[15]])

qc.append(RZGate(0.1194574129642972), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[16]])

qc.append(RZGate(0.2389148259285944), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[17]])

qc.append(RZGate(0.4778296518571888), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[18]])

qc.append(RZGate(0.05226261817188003), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[9], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[11]])

qc.append(RZGate(8.581710701458131e-05), [q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[11]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[12]])

qc.append(RZGate(0.00017163421402916263), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[13]])

qc.append(RZGate(0.00034326842805832526), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[14]])

qc.append(RZGate(0.0006865368561166505), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[15]])

qc.append(RZGate(0.001373073712233301), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[16]])

qc.append(RZGate(0.002746147424466602), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[17]])

qc.append(RZGate(0.005492294848933204), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[18]])

qc.append(RZGate(0.0006007197491020692), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[10], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[12]])

qc.append(RZGate(0.00034326842805832526), [q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[12]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[13]])

qc.append(RZGate(0.0006865368561166505), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[14]])

qc.append(RZGate(0.001373073712233301), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[15]])

qc.append(RZGate(0.002746147424466602), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[16]])

qc.append(RZGate(0.005492294848933204), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[17]])

qc.append(RZGate(0.010984589697866408), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[18]])

qc.append(RZGate(0.0012014394982041384), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[11], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[13]])

qc.append(RZGate(0.001373073712233301), [q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[13]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[14]])

qc.append(RZGate(0.002746147424466602), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[15]])

qc.append(RZGate(0.005492294848933204), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[16]])

qc.append(RZGate(0.010984589697866408), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[17]])

qc.append(RZGate(0.021969179395732816), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[18]])

qc.append(RZGate(0.002402878996408277), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[12], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[14]])

qc.append(RZGate(0.005492294848933204), [q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[14]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[15]])

qc.append(RZGate(0.010984589697866408), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[16]])

qc.append(RZGate(0.021969179395732816), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[17]])

qc.append(RZGate(0.04393835879146563), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[18]])

qc.append(RZGate(0.004805757992816554), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[13], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[15]])

qc.append(RZGate(0.021969179395732816), [q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[15]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[16]])

qc.append(RZGate(0.04393835879146563), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[17]])

qc.append(RZGate(0.08787671758293127), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[18]])

qc.append(RZGate(0.009611515985633107), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[14], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[16]])

qc.append(RZGate(0.08787671758293127), [q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[16]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[17]])

qc.append(RZGate(0.17575343516586253), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[18]])

qc.append(RZGate(0.019223031971266215), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[15], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[16], q[17]])

qc.append(RZGate(0.35150687033172506), [q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[16], q[17]])

qc.append(XGate().control(1, ctrl_state='1'), [q[16], q[18]])

qc.append(RZGate(0.03844606394253243), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[16], q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[17], q[18]])

qc.append(RZGate(0.07689212788506486), [q[18]])

qc.append(XGate().control(1, ctrl_state='1'), [q[17], q[18]])

qc.append(RXGate(1.5707963267948966), [q[0]])

qc.append(RXGate(1.5707963267948966), [q[1]])

qc.append(RXGate(1.5707963267948966), [q[2]])

qc.append(RXGate(1.5707963267948966), [q[3]])

qc.append(RXGate(1.5707963267948966), [q[4]])

qc.append(RXGate(1.5707963267948966), [q[5]])

qc.append(RXGate(1.5707963267948966), [q[6]])

qc.append(RXGate(1.5707963267948966), [q[7]])

qc.append(RXGate(1.5707963267948966), [q[8]])

qc.append(RXGate(1.5707963267948966), [q[9]])

qc.append(RXGate(1.5707963267948966), [q[10]])

qc.append(RXGate(1.5707963267948966), [q[11]])

qc.append(RXGate(1.5707963267948966), [q[12]])

qc.append(RXGate(1.5707963267948966), [q[13]])

qc.append(RXGate(1.5707963267948966), [q[14]])

qc.append(RXGate(1.5707963267948966), [q[15]])

qc.append(RXGate(1.5707963267948966), [q[16]])

qc.append(RXGate(1.5707963267948966), [q[17]])

qc.append(RXGate(1.5707963267948966), [q[18]])

qc.measure(q[0], c[0])

qc.measure(q[1], c[1])

qc.measure(q[2], c[2])

qc.measure(q[3], c[3])

qc.measure(q[4], c[4])

qc.measure(q[5], c[5])

qc.measure(q[6], c[6])

qc.measure(q[7], c[7])

qc.measure(q[8], c[8])

qc.measure(q[9], c[9])

qc.measure(q[10], c[10])

qc.measure(q[11], c[11])

qc.measure(q[12], c[12])

qc.measure(q[13], c[13])

qc.measure(q[14], c[14])

qc.measure(q[15], c[15])

qc.measure(q[16], c[16])

qc.measure(q[17], c[17])

qc.measure(q[18], c[18])


# Draw
print(qc.draw())


# Execution (Local Aer Simulator)
print("Simulating circuit with Aer Simulator...")
simulator = AerSimulator()
transpiled_qc = transpile(qc, simulator)
result = simulator.run(transpiled_qc, shots=1024).result()
counts = result.get_counts()
print("Counts:", counts)


# ================================================================
# GENERATED T3 DOMAIN DECODING + INDEPENDENT CLASSICAL BASELINE
# ================================================================
from itertools import combinations as _tacs_combinations
_tacs_qubo_vars = ['x_A', 'x_B', 'x_C', 'x_D', 'x_E', 'x_F', 'x_G', 'x_H', 'x_I', 'x_J', 's_1', 's_2', 's_3', 's_4', 's_5', 's_6', 's_7', 's_8', 's_9']
_tacs_projects = {'A': {'cost': 55, 'benefit': 95}, 'B': {'cost': 10, 'benefit': 4}, 'C': {'cost': 47, 'benefit': 60}, 'D': {'cost': 5, 'benefit': 32}, 'E': {'cost': 4, 'benefit': 23}, 'F': {'cost': 50, 'benefit': 72}, 'G': {'cost': 8, 'benefit': 80}, 'H': {'cost': 61, 'benefit': 62}, 'I': {'cost': 85, 'benefit': 65}, 'J': {'cost': 87, 'benefit': 46}}
_tacs_budget = 269
_tacs_slack_weights = [1, 2, 4, 8, 16, 32, 64, 128, 14]

_tacs_project_ids = tuple(sorted(_tacs_projects))
_tacs_total_shots = sum(counts.values())
if _tacs_total_shots <= 0:
    raise ValueError("Aer returned no measurement counts")

# Classical exhaustive search. Independent of any measured bitstring.
_tacs_optimum = -1
_tacs_optimal_selections = set()
for _r in range(len(_tacs_project_ids) + 1):
    for _choice in _tacs_combinations(_tacs_project_ids, _r):
        _cost = sum(_tacs_projects[_p]["cost"] for _p in _choice)
        if _cost > _tacs_budget:
            continue
        _benefit = sum(_tacs_projects[_p]["benefit"] for _p in _choice)
        if _benefit > _tacs_optimum:
            _tacs_optimum = _benefit
            _tacs_optimal_selections = {_choice}
        elif _benefit == _tacs_optimum:
            _tacs_optimal_selections.add(_choice)
assert _tacs_optimum >= 0

# Counts in Qiskit are big-endian display strings; bit i is counted
# from the RIGHT. T2 measures qubit i into classical bit i.
_tacs_domain_counts = {}
_tacs_domain_feasible = 0
_tacs_full_qubo_feasible = 0
_tacs_optimal_domain = 0
_tacs_optimal_full_qubo = 0
for _display_bits, _frequency in counts.items():
    _bits = ''.join(_ch for _ch in _display_bits if _ch in '01')
    if len(_bits) != len(_tacs_qubo_vars):
        raise ValueError(f"Unexpected Qiskit bitstring: {_display_bits!r}")
    _chosen = []
    _unused_budget = 0
    for _i, _bit in enumerate(reversed(_bits)):
        if _bit == '0':
            continue
        _name = _tacs_qubo_vars[_i]
        if _name.startswith('x_'):
            _chosen.append(_name[2:])
        elif _name.startswith('s_'):
            _index = int(_name[2:]) - 1
            _unused_budget += _tacs_slack_weights[_index]
        else:
            raise ValueError(f"Unexpected QUBO variable: {_name!r}")
    _selection = tuple(sorted(_chosen))
    _cost = sum(_tacs_projects[_p]['cost'] for _p in _selection)
    _is_domain_feasible = _cost <= _tacs_budget
    _is_qubo_feasible = _cost + _unused_budget == _tacs_budget
    _tacs_domain_counts[_selection] = _tacs_domain_counts.get(_selection, 0) + _frequency
    if _is_domain_feasible:
        _tacs_domain_feasible += _frequency
    if _is_qubo_feasible:
        _tacs_full_qubo_feasible += _frequency
    if _selection in _tacs_optimal_selections:
        _tacs_optimal_domain += _frequency
        if _is_qubo_feasible:
            _tacs_optimal_full_qubo += _frequency

_tacs_measured_feasible = [
    _selection for _selection in _tacs_domain_counts
    if sum(_tacs_projects[_p]['cost'] for _p in _selection) <= _tacs_budget
]
_tacs_best_measured = max(
    _tacs_measured_feasible,
    key=lambda _sel: (sum(_tacs_projects[_p]['benefit'] for _p in _sel),
                      -sum(_tacs_projects[_p]['cost'] for _p in _sel)),
    default=None,
)
_tacs_best_measured_benefit = (
    sum(_tacs_projects[_p]['benefit'] for _p in _tacs_best_measured)
    if _tacs_best_measured is not None else None
)
_tacs_ratio = (
    (_tacs_best_measured_benefit / _tacs_optimum if _tacs_optimum > 0 else 1.0)
    if _tacs_best_measured_benefit is not None else 0.0
)

print("\n=== Classical baseline (exact brute force) ===")
print(f"Budget: {_tacs_budget}")
print(f"Optimal benefit: {_tacs_optimum}")
print(f"Optimal project selections: {sorted(_tacs_optimal_selections)}")
print("\n=== QAOA measurement validation ===")
print(f"Shots: {_tacs_total_shots}")
print(f"Best feasible selection measured: {_tacs_best_measured}")
print(f"Best measured benefit: {_tacs_best_measured_benefit}")
print(f"Approximation ratio (best measured / optimum): {_tacs_ratio:.4f}")
print(f"Domain-feasible observations: {100*_tacs_domain_feasible/_tacs_total_shots:.2f}%")
print(f"QUBO-feasible observations (consistent slack): {100*_tacs_full_qubo_feasible/_tacs_total_shots:.2f}%")
print(f"Optimal project selections measured: {100*_tacs_optimal_domain/_tacs_total_shots:.2f}%")
print(f"Optimal full QUBO states measured: {100*_tacs_optimal_full_qubo/_tacs_total_shots:.2f}%")
print("\nTop 5 measured project selections (slack aggregated):")
for _selection, _count in sorted(
    _tacs_domain_counts.items(), key=lambda kv: (-kv[1], kv[0])
)[:5]:
    _cost = sum(_tacs_projects[_p]['cost'] for _p in _selection)
    _benefit = sum(_tacs_projects[_p]['benefit'] for _p in _selection)
    print(f"  {_selection}: {_count/_tacs_total_shots:.2%}, cost={_cost}, "
          f"benefit={_benefit}, feasible={_cost <= _tacs_budget}")
