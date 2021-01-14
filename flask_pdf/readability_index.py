from textstat import textstat

text = """In this case, it is easy to see that if we do not maintain the data dependence
involving R2, we can change the result of the program. Less obvious is the fact
that if we ignore the control dependence and move the load instruction before the
branch, the load instruction may cause a memory protection exception. Notice
that no data dependence prevents us from interchanging the BEQZ and the LW; it is
only the control dependence. To allow us to reorder these instructions (and still
preserve the data dependence), we would like to just ignore the exception when
the branch is taken. In Section 3.6, we will look at a hardware technique, speculation, which allows us to overcome this exception problem. Appendix H looks at
software techniques for supporting speculation.
The second property preserved by maintenance of data dependencies and control dependencies is the data flow. The data flow is the actual flow of data values
among instructions that produce results and those that consume them. Branches
make the data flow dynamic, since they allow the source of data for a given
instruction to come from many points. Put another way, it is insufficient to just
maintain data dependencies because an instruction may be data dependent on
more than one predecessor. Program order is what determines which predecessor
will actually deliver a data value to an instruction. Program order is ensured by
maintaining the control dependencies."""

text2 = """Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.
The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.
The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.
The next day, a wolf happened to pass by the lane where the three little pigs lived; and he saw the straw house, and he smelled the pig inside. He thought the pig would make a mighty fine meal and his mouth began to water."""

text3 = """The Domain Name System (DNS) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It associates various information with domain names assigned to each of the participating entities. Most prominently, it translates more readily memorized domain names to the numerical IP addresses needed for locating and identifying computer services and devices with the underlying network protocols. By providing a worldwide, distributed directory service, the Domain Name System has been an essential component of the functionality of the Internet since 1985.
The Domain Name System delegates the responsibility of assigning domain names and mapping those names to Internet resources by designating authoritative name servers for each domain. Network administrators may delegate authority over sub-domains of their allocated name space to other name servers. This mechanism provides distributed and fault-tolerant service and was designed to avoid a single large central database.
The Domain Name System also specifies the technical functionality of the database service that is at its core. It defines the DNS protocol, a detailed specification of the data structures and data communication exchanges used in the DNS, as part of the Internet Protocol Suite."""

with open('internet_texts_examples/example1.txt', encoding="utf-8") as text11:
    print(textstat.flesch_reading_ease(text11.read()))

with open('internet_texts_examples/example2.txt', encoding="utf-8") as text22:
    print(textstat.flesch_reading_ease(text22.read()))

with open('internet_texts_examples/example3.txt', encoding="utf-8") as text33:
    print(textstat.flesch_reading_ease(text33.read()))

with open('internet_texts_examples/example4.txt', encoding="utf-8") as text44:
    print(textstat.flesch_reading_ease(text44.read()))