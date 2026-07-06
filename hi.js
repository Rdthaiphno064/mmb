const now = new Date();
const expires = new Date(now.getTime() + 24 * 60 * 60 * 1000);
$done({
  response: {
    status: 200,
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      valid: true,
      product: {
        _id: "69d5456480caeb029780d8ab",
        name: Aovcheat VN",
        bundle: "com.garena.game.kgvn1"
      },
      deviceId: "f5c444bdcfe54aa09fd5dc7abd26dbd6",
      activatedAt: now.toISOString(),
      expiresAt: expires.toISOString(),
      duration: "1d",
      needUdid: false,
      authToken: {
        data: "eyJrIjoiQW92Y2hlYXRWTl8xZF9hMTRhZjBkMmU2NTNiYmQ5IiwiZCI6ImY1YzQ0NGJkY2ZlNTRhYTA5ZmQ1ZGM3YWJkMjZkYmQ2IiwiZSI6MTc4MzQxNTA2MTUyMywibiI6IjQxYTcyNzE0M2ViMzc3MzBhMzI1MmRlYzliOGRiZGIzM2JlMDJmNDJlNmJlMzY4N2RmMjNmOWU2Y2I5YWY4ZmQiLCJ0IjoxNzgzMzI4NjYxNTI2fQ==",
        sig: "I23cq1kx/Duq9ZD6kZwRxUPHnws5Jh4PpJbfkTxkUI5HNJ7VAEmv6CAOrX9UV+koiY9b9JipYJj2A3au4eOqh1nMNJ1t/mFYmSLPVSKj6THZA22uXggqT1TsUhk8ZUmO6TYQPr12bAT+mkq0DIZcE4YPBKg2xiEPWgg1Zsnh/cICB2+gvMJQBBymGIUCpgH3mpeA06ykSnV5L5lktmfYga0vTr5/KG57oFxnQSkrLxfG6i5dyr5JLh4B65kQ+dLnLhyr2nJNXTE51luDbuR7aFSPM3UaH/pNKF9bq7uprjqh91OdyxDF9c96kt6ZR1FXawkjsbzNKBdUbksKVpHNRA=="
      }
    }, null, 2)
  }
});
