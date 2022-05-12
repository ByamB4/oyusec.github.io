package auth

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"encoding/pem"
	"fmt"
	"io/ioutil"

	"github.com/golang-jwt/jwt"
)

type (
	GJWT struct {
		private *ecdsa.PrivateKey
		pub     *ecdsa.PublicKey
		timeout int
	}
	Claims struct {
		jwt.StandardClaims
		IsActive bool    `json:"isActive"`
		Address  *string `json:"address"`
		ID       uint64  `json:"id"`
		Role     uint8   `json:"role"`
	}
)

func Write() {
	g := GJWT{}
	g.private, _ = ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	g.pub = &g.private.PublicKey
	data := elliptic.Marshal(g.pub.Curve, g.pub.X, g.pub.Y)
	pubBytes := pem.EncodeToMemory(&pem.Block{
		Type:  "Basic ES256",
		Bytes: data,
	})

	ioutil.WriteFile("pub.pem", pubBytes, 0644)
	data = elliptic.Marshal(g.private.Curve, g.private.X, g.private.Y)

	pubBytes = pem.EncodeToMemory(&pem.Block{
		Type:  "Basic ES256",
		Bytes: data,
	})

	ioutil.WriteFile("pri.pem", pubBytes, 0644)
}

func New(private, public string, timeout int) (*GJWT, error) {
	var (
		key    []byte
		result GJWT
	)

	result.timeout = timeout
	key, err := ioutil.ReadFile(private)
	if err != nil {
		return nil, err
	}
	result.private, err = jwt.ParseECPrivateKeyFromPEM([]byte(key))
	if err != nil {
		return nil, err
	}
	key, err = ioutil.ReadFile(public)
	if err != nil {
		return nil, err
	}
	result.pub, err = jwt.ParseECPublicKeyFromPEM([]byte(key))
	return &result, err
}

func (g *GJWT) Read(inToken string) (*Claims, error) {
	var t Claims
	if _, err := jwt.ParseWithClaims(inToken, &t, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodECDSA); !ok {
			return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
		}
		return g.pub, nil
	}); err != nil {
		return nil, err
	}
	return &t, nil
}
