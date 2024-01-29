function solution(numer1, denom1, numer2, denom2) {
    let denom = denom1 * denom2;
    numer1 *= denom2;
    numer2 *= denom1;
    let numer = numer1 + numer2;
    
    // 최대공약수 구하는 함수
    const gcd = (a, b) => {
        return b === 0 ? a : gcd(b, a % b);
    };

    const commonFactor = gcd(numer, denom);
    numer /= commonFactor;
    denom /= commonFactor;

    return [numer, denom];
}
