"""
in: keywords set
out: best cluster (range-like) found in text
"""

import spacy
import pytextrank

# example text
text = """Mandatory Access Control Models

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea

Department of Computer Science
Alexandru Ioan Cuza University of Ia¸si
Ia¸si, Romania
E-mail: ferucio.tiplea@uaic.ro

Outline

1

2

Introduction to MAC

Information Flow Models

3 Conﬁdentiality-based Mandatory Policies: The Bell-LaPadula Model

4

Integrity-based Mandatory Policies: The Biba Model

5 Combining the BLP and Biba Models

6 The Chinese Wall Model

7 MAC Implementations

8 Concluding Remarks on MAC Models

Mandatory Access Control

Introduction to MAC

Basic features:

MAC enforces access control on the basis of regulations mandated by a
central authority

No concept of ownership in MAC

MAC makes distinction between users and subjects

MAC models:

The Bell-LaPadula model

The Biba model

The Chinese-wall model

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

3 / 26

Information Flow Models

Information Flow Models

D. E. Denning. A Lattice Model of Secure Information Flow,
Communications of the ACM, vol.19, no. 5, 1976, 236–243.

Basic features:

IF models are concerned with the ﬂow of information from one security
class to another

Object = viewed as a container of information

Examples of objects: ﬁles or directories in an operating system, or
relations and tuples in a database

Information ﬂow is controlled by assigning every object a security class or
security label

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

4 / 26

Information Flow Models

Information Flow Models: Deﬁnition

Deﬁnition 1

An information ﬂow model is a triple (SC, →, ⊕), where:

SC is a set of elements called security classes

→ ⊆ SC × SC is a binary relation called may-ﬂow

⊕ : SC × SC→SC is a commutative and associative operator called the
class combiner operator

Meaning:

A→B : the information may ﬂow from the security class A to the security
class B

A ⊕ B : if information from the two security classes A and B are combined,
the result belongs to the security class A ⊕ B

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

5 / 26

Information Flow Models

Information Flow Models: Denning’s Axioms

Denning’s axioms:

Axiom 1: SC is ﬁnite

Axiom 2: The may-ﬂow relation → is a partial order

Axiom 3: SC has a least element w.r.t. →

Axiom 4: ⊕ is a least upper bound operator

Proposition 1

Any information ﬂow model that satisﬁes the Denning’s axioms is a lattice.

In what follows, all IF models we consider satisfy the Denning’s axioms !

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

6 / 26

Information Flow Models

Information Flow Models: Dominance

Deﬁnition 2

Let (SC, →, ⊕) be an information ﬂow model and A, B ∈ SC. We say that A
dominates B, denoted A ≥ B, if B→A.

Notation and terminology:

A > B (A strictly dominates B) if A dominates B and A (cid:54)= B

A and B are comparable if A ≥ B or B ≥ A

A and B are incomparable if A and B are not comparable

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

7 / 26

Information Flow Models

Information Flow Models: Examples

H

L

/0

A1

An

H

· · ·

L

TS

S

C

U

{A, B, C}

{ /0}

{A, B}

{A}

{B}

{A, B}

{A}

{A, C}

{B, C}

{B}

{C}

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

8 / 26

Conﬁdentiality-based Mandatory Policies: The Bell-LaPadula Model

Conﬁdentiality-based Mandatory Policies

Aim: control the direct and indirect ﬂows of information by preventing
leakages to unauthorized subjects

Subjects and objects are assigned security levels (security classes)

The security level of an object, also called security classiﬁcation, reﬂects
the sensitivity of the information contained in the object

The security level of a subject, also called security clearance, reﬂects the
user’s trustworthiness

Requests of subjects to access objects are regulated by means of their
security classes

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

9 / 26

Conﬁdentiality-based Mandatory Policies: The Bell-LaPadula Model

The Bell-LaPadula Model: A Minimalist Approach

D. E. Bell, L. J. LaPadula. Secure Computer Systems: Mathematical
Foundations, MITRE Corporation, 1973.

Overview:

Key idea: augment DAC with MAC to enforce information ﬂow policies

Two-step approach:

1 First, an access control matrix D is established

2 Second, operations must be authorized by the mandatory access control

policy

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

10 / 26

Conﬁdentiality-based Mandatory Policies: The Bell-LaPadula Model

The Bell-LaPadula Model: A Minimalist Approach

The MAC in the BLP model:

associate labels to subjects and objects by some function λ (once
assigned, labels cannot be changed – this is called tranquility)

Rules (No Read Up – No Write Down):

1 Simple security (ss-) property – s is allowed to read o only if λ (s) ≥ λ (o)

2 ∗-property – s is allowed to write o only if λ (s) ≤ λ (o)

Remark 1

The ∗-property allows secret data be destroyed or damaged by unclassiﬁed
subjects. To prevent this the ∗-property is sometimes used in the form

Strong ∗-property – s is allowed to write o only if λ (s) = λ (o)

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

11 / 26

Conﬁdentiality-based Mandatory Policies: The Bell-LaPadula Model

The Bell-LaPadula Model: Remarks

In some approaches, write access means “read and write”, with append
access provided for “write only”

The BLP model is stated in terms of read and write operations (which
sufﬁces to illustrate the main points). Other operations may be added,
such as create and destroy objects, constrained by the ∗-property
because they modify the state of the object in question

Mandatory controls in BLP are coupled with discretionary control: if the
access control matrix does not authorizes the operation, there is no need
to check the mandatory controls since the operation will be rejected
anyway

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

12 / 26

Integrity-based Mandatory Policies: The Biba Model

Integrity-based Mandatory Policies

Aim: control the ﬂows of information and prevent subjects to indirectly
modify information they cannot write

Subjects and objects are assigned integrity levels (integrity classes)

The integrity level of an object reﬂects both the degree of trust of the
information stored in the object and the potential damage resulting from
unauthorized modiﬁcations of the information

The integrity level of a subject reﬂects the user’s trustworthiness for
inserting, modifying, or deleting information

Requests of subjects to access objects are regulated by means of their
integrity classes

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

13 / 26

Integrity-based Mandatory Policies: The Biba Model

The Biba Model

K. J. Biba. Integrity Considerations for Secure Computer Systems,
MTR-3153, The Mitre Corporation, April 1977.

The MAC in the Biba model:

associate labels to subjects and objects by some function ω

Rules (No Read Down – No Write Up):

1 Simple integrity (si-) property – s is allowed to read o only if ω(s) ≤ ω(o)

2

Integrity ∗-property – s is allowed to write o only if ω(s) ≥ ω(o)

Remark 2

The Biba model’s rules are the dual of the BLP model’s rules.

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

14 / 26

Combining the BLP and Biba Models

Combining the BLP and Biba Models

There is no fundamental difference between the BLP and Biba models:
both are concerned with information ﬂow in a lattice of security classes

In the BLP model, the information ﬂows upward

In the Biba model, the information ﬂows downward

The direction is irrelevant: it is a matter of convention in representing the
highest security class (in our case, in both the BLP and Biba models the
highest security class on top of the lattice)

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

15 / 26

Combining the BLP and Biba Models

Case 1: Single Label

Combination 1: use a single label for both conﬁdentiality and integrity

Conclusions:

s can read or write o only if s and o have the same security class !

No information ﬂow between security classes !

Irrelevant model

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

16 / 26

Combining the BLP and Biba Models

Case 2: Independent Labels, Same Directions

Combination 2: use independent labels for conﬁdentiality (λ ) and integrity (ω)
under the assumption that both lattices have the highest security class on top

Conclusions:

Rules:

1

2

s is allowed to read o only if λ (s) ≥ λ (o) and ω(s) ≤ ω(o)

s is allowed to write o only if λ (s) ≤ λ (o) and ω(s) ≥ ω(o)

The model uses two lattices with information ﬂow going in opposite
directions

Implemented in several operating system, database, and network
products

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

17 / 26

Combining the BLP and Biba Models

Case 3: Independent Labels, Opposite Directions

Combination 3: use independent labels for conﬁdentiality (λ ) and integrity (ω)
under the assumption that the lattices have the highest security classes on
opposite directions

Conclusions:

Rules:

1

2

s is allowed to read o only if λ (s) ≥ λ (o) and ω(s) ≥ ω(o)

s is allowed to write o only if λ (s) ≤ λ (o) and ω(s) ≤ ω(o)

The two lattices can be combined in just one lattice (see next slide)

In this lattice, the entity with highest conﬁdentiality has lowest integrity,
and vice versa

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

18 / 26

Combining the BLP and Biba Models

Case 3: Example

highest conﬁdentiality

λH

λL

ωL

ωH

highest integrity

highest conﬁdentiality, lowest integrity

λHωH

λLωL

lowest conﬁdentiality, highest integrity

w
o
ﬂ
n
o
i
t
a
m
r
o
f
n

i

λHωL

λLωH

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

19 / 26

The Chinese Wall Model

The Chinese Wall Model

D. F. C. Brewer, M. J. Nash. The Chinese Wall security policy, IEEE
Symposium on Security and Privacy, 206–214, 1989.

Where it arises:

In the commercial sector that provides consulting services to other
companies

Aim:

How:

Prevent information ﬂows that result in a conﬂict of interest and
inadvertent disclosure of information by a consultant or contractor
Example of conﬂict of interest: lawyer providing consultancy services for
two airline companies

Combines commercial discretion with legally enforceable mandatory
controls

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

20 / 26

The Chinese Wall Model

The Chinese Wall Model

Basic elements:

Object = item of information concerning a single corporation (company)

Company dataset = all objects which concern the same company

Conﬂict of interest class = all datasets of the companies that are in
competition

Subject = user or program that might act on behalf of a user

Basic idea:

In the ﬁrst instance, each subject has complete freedom to access
anything he cares

Once an object in a dataset D of some conﬂict of interest class CoI is
chosen, a Chinese Wall is created around D and no other dataset in CoI
can be chosen by the same subject.

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

21 / 26

The Chinese Wall Model

The Chinese Wall Model

Rules:

(Chinese Wall) Simple Security Rule: a subject s can be granted read
access to an object o only if the object:

1

is in the same company datasets as the objects already accessed by s, that
is, “within the Wall”, or

2 belongs to an entirely different conﬂict of interest class

(Chinese Wall) ∗-property: a subject s can be granted write access to an
object o only if:

1

s can read o by the simple security rule, and

2 no object can be read which is in a different company dataset to the one for

which write access is requested

The Chinese Wall model can be states as an information ﬂow model !

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

22 / 26

MAC Implementations

MAC Implementations

Early implementations of MAC (started out in the eighties):

Honeywell Secure Communications Processor (SCOMP), Strategic Air
Command DIgital Network (SACDIN) of the US Air Force (USAF), Boeing
Multi-level Secure Local Area Network, etc.

These are focused to protect military-oriented security classiﬁcation levels

More recent implementations of MAC:

Security-Enhanced Linux (SELinux) : Linux kernel security module,
incorporated into Linux kernels from 2.6, to provide the mechanism for
supporting access control security policies

Mandatory Integrity Control (MIC) : incorporated by Microsoft starting
with Windows Vista and Windows Server 2008, adds integrity levels

etc.

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

23 / 26

MAC Implementations

Mandatory Integrity Control (MIC)

MAC implementation in Windows Vista is called Mandatory Integrity
Control (MIC), which is a form of the Biba model

It ensures integrity by controlling writes and deletions: to write to or
delete an object, the subject’s integrity level must be greater than or
equal to the object’ integrity level

There are six integrity levels: Untrusted, Low (everyone), Medium
(standard users, authenticated users), High (local services, network
services, elevated users), System (system services), and Trusted Installer

Subjects’ integrity level: when a user logs on, Windows Vista assigns an
integrity SID to the user’s access token

Objects’ integrity level: ﬁles, pipes, threads, registry keys, printers etc.,
are assigned an integrity SID which is stored in the System Access
Control List (SACL)

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

24 / 26

MAC Implementations

Security-Enhanced Linux (SELinux)

Subject security level = domain

Object security level = type

Type of an object = class

Two types of rules: access rules and labeling rules

Access rules:

Example: allow sshd.t shell.exec.t:file execute

Meaning: when a subject of sshd.t accesses an object of shell.exec.t
of class file, it has the execute permission

Rules for the type of a new object (labeling rules):

Example: type.transition sshd.t tmp.t: devfile.class.set
cardmsg.dev.t

Meaning: when sshd daemon creates a device ﬁle in the tmp directory, the
new ﬁle is labeled with cardmsg.dev.t

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

25 / 26

Concluding Remarks on MAC Models

Concluding Remarks

MAC provides protection against indirect information leakages

MAC is still vulnerable to covert channels

covert channels were introduced by Lampson in 1973 as

“channels not intended for information transfer at all, such as the service
program’s effect on system load.”

Example: a low level subject requires a resource which is busy by a high
level subject. If the system signal this to the low level subject, then there is a
ﬂow of information from the high level subject to the low level subject

Covert channels can exist in any MAC system that restrict information ﬂow

Covert channels are hard to detect and control

Prof.Dr. Ferucio Lauren¸tiu ¸Tiplea (UAIC)

Mandatory Access Control Models

26 / 26"""

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

doc = nlp(text)

# examine the top-ranked phrases in the document
k = 0
for p in doc._.phrases:
    print("{}".format(p.text))
    k += 1
    if k == 20:
        break
