# Crypto II Writeup

Name: Barath Srinivasan
Section: 0202

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Barath Srinivasan

## Assignment Writeup

### Part 1 (70 Pts)

CMSC389R-{m3ss@g3_!n_A_b0ttl3}

### Part 2 (30 Pts)

1) What I notice about the two pictures is that they are the original image but because of the encryption we used they became very grainy and noisy. This is meant as a way to hide what the image was originally.
2) ECB is much less secure than CBC because in ECB you can still see the what the original image was supposed to be to an extent. However, with CBC all you see is static. As, the reason why this ECB is less secure is because it just runs the image through the encryption process once, like a input/output function. However, CBC works by using blocks and gradually building the encryption. This means with CBC there is a extra level os security because each level of encryption is dependent on the previous level, while with ECB there isn't that level of security.
