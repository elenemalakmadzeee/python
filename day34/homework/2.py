# შექმენით manual_range ფუნქცია, რომელიც იქნება range ფუნქციის კოლნი, ამ ფუნქციას უნდა ჰქონდეს 3 არგუმენტი, მაგრამ თუ გამოძახებისას გადაეცა მხოლოდ 1 არგუმენტი default-ად start-ის მნიშვნელობა იქნება 0 და step-ის 1. ხოლო 2 არგუმენტის შემთხვევაში მხოლოდ step-ი იქნება 1.

#გაიხსენეთ, რომ range ფუნქციას გადაეცემა 3 პარამეტრი start, end, step
def manual_range(end, start = 0, step = 1):
    while start <= end:
        print(start)
        start += step
    
manual_range(10, 1, 2)