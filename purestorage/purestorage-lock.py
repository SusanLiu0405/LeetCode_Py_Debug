def check_locks(events):
    stack = []
    lock_set = set()

    for i, event in enumerate(events):	# 直接获得索引i
        command, lock_id = event.split()
        lock_id = int(lock_id)

        if command == "ACQUIRE":
            if lock_id in lock_set:
                return i + 1
            stack.append(lock_id)
            lock_set.add(lock_id)
        elif command == "RELEASE":
            if not stack or stack[-1] != lock_id:
                return i + 1
            stack.pop()
            lock_set.remove(lock_id)

    if stack:
        return len(events) + 1

    return 0

if __name__ == '__main__':
	events1 = [
		"ACQUIRE 364",
		"ACQUIRE 84",
		"RELEASE 84",
		"RELEASE 364"
	]

	events2 = [
		"ACQUIRE 364",
		"ACQUIRE 84",
		"RELEASE 364",
		"RELEASE 84"
	]

	events3 = [
		"ACQUIRE 84",
		"RELEASE 84",
		"ACQUIRE 84",
		"RELEASE 84",
	]

	print(check_locks(events1))  # 0
	print(check_locks(events2))  # 3
	print(check_locks(events3))  # 0
