def restoreIpAddresses(s: str) -> list[str]:
    def generateValidIPs(start, path):
        # If we've formed 4 segments and used up all characters, it's valid
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Try to form segments of i 1, 2, or 3
        for i in range(1, 4):
            # If the segment exceeds the remaining string, break
            if start + i > len(s):
                break

            segment = s[start:start + i]

            # Validate the segment
            if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                continue

            # Add the segment to the path and recurse
            generateValidIPs(start + i, path + [segment])

    result = []
    generateValidIPs(0, [])
    return result


# Example Usage
print(restoreIpAddresses("25525511135"))