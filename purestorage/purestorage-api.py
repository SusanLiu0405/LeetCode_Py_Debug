import requests


def bestRestaurant(city, max_cost):
	base_url = "https://jsonmock.hackerrank.com/api/food_outlets"
	page = 1
	best_outlet = None
	best_rating = -1
	lowest_cost = float('inf')

	while True:
		url = f"{base_url}?city={city}&page={page}"
		response = requests.get(url)
		data = response.json()

		# 遍历当前页的餐馆数据
		for outlet in data['data']:
			outlet_cost = outlet['estimated_cost']
			rating = outlet['user_rating']['average_rating']

			# 检查是否符合成本要求和是否具有更高的评分
			if outlet_cost <= max_cost:
				if (rating > best_rating) or (rating == best_rating and outlet_cost < lowest_cost):
					best_outlet = outlet
					best_rating = rating
					lowest_cost = outlet_cost

		# 检查是否还有更多页
		if page >= data['total_pages']:
			break
		page += 1

	return best_outlet


if __name__ == '__main__':
	# Example
	city = "Chicago"
	cost = 100
	result = bestRestaurant(city, cost)
	print(result)
